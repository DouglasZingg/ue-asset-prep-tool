import json
import os
import unreal


def _try_len(obj, attr_names):
    """Try several attribute names and return len(list) if found."""
    for name in attr_names:
        try:
            v = getattr(obj, name)
            return len(v)
        except Exception:
            pass
        try:
            v = obj.get_editor_property(name)
            return len(v)
        except Exception:
            pass
    return 0


def _count_simple_collision_prims(static_mesh: unreal.StaticMesh) -> int:
    """
    Count simple collision primitives (box/sphere/capsule/convex).
    Uses multiple access patterns to handle API differences.
    """
    # 1) Try EditorStaticMeshLibrary (often available in Python even when BP nodes are missing)
    try:
        lib = unreal.EditorStaticMeshLibrary
        # introspect common function names
        for fn_name in ["get_simple_collision_count", "get_simple_collision_primitives_count"]:
            if hasattr(lib, fn_name):
                return int(getattr(lib, fn_name)(static_mesh))
    except Exception:
        pass

    # 2) Read BodySetup/AggGeom directly
    try:
        body_setup = static_mesh.get_editor_property("body_setup")
        if not body_setup:
            return 0

        agg = body_setup.get_editor_property("agg_geom")
        if not agg:
            return 0

        # Try both snake_case and CamelCase names (and editor_property lookups)
        box_count = _try_len(agg, ["box_elems", "BoxElems"])
        sphere_count = _try_len(agg, ["sphere_elems", "SphereElems"])
        sphyl_count = _try_len(agg, ["sphyl_elems", "SphylElems"])
        convex_count = _try_len(agg, ["convex_elems", "ConvexElems"])

        return int(box_count + sphere_count + sphyl_count + convex_count)
    except Exception:
        return 0


def check_static_mesh_collision(asset_path: str, out_json_path: str) -> None:
    result = {
        "asset_path": asset_path,
        "asset_type": "StaticMesh",
        "collision_count": 0,
        "has_collision": False,
        "loaded_name": "",
        "loaded_path": "",
        "error": ""
    }

    try:
        asset = unreal.EditorAssetLibrary.load_asset(asset_path)
        if not asset:
            result["error"] = "Could not load asset"
        elif not isinstance(asset, unreal.StaticMesh):
            result["error"] = f"Not a StaticMesh: {type(asset)}"
        else:
            result["loaded_name"] = asset.get_name()
            try:
                result["loaded_path"] = asset.get_path_name()
            except Exception:
                result["loaded_path"] = asset_path

            count = _count_simple_collision_prims(asset)
            result["collision_count"] = int(count)
            result["has_collision"] = (count > 0)

    except Exception as e:
        result["error"] = str(e)

    out_dir = os.path.dirname(out_json_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    with open(out_json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    unreal.log(f"[AssetPrep] CollisionCheck wrote {out_json_path} -> {result}")
