#!/usr/bin/env python

import sys
import os
import json

from sys import argv
from argparse import ArgumentParser
from pathlib import Path

# enables importing from parent directories
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from class__main.menus.dmenu import Dmenu
from class__main.menus.fuzzel import Fuzzel

from class__main.window_managers.dwm import Dwm
from class__main.window_managers.hyprland import Hyprland


def setup_wm(
    menu: str, wm: str, wallpaper_dict: dict, colorschemes: dict
) -> Dwm | Hyprland:
    if menu == "dmenu":
        menu_obj = Dmenu(
            width=600,
            line=len(colorschemes),
        )
    elif menu == "fuzzel":
        menu_obj = Fuzzel(
            width=50,
            line=10,
        )
    else:
        sys.exit(f"Menu - '{menu}' is not recognized!\n")

    if wm == "dwm":
        wm_obj = Dwm(
            menu=menu_obj,
            wallpaper_dict=wallpaper_dict,
            colorscheme_dict=colorschemes,
        )
    elif wm == "hyprland":
        wm_obj = Hyprland(
            menu=menu_obj,
            wallpaper_dict=wallpaper_dict,
            colorscheme_dict=colorschemes,
        )

    else:
        sys.exit(f"Window manager - '{wm}' is not recognized!\n")

    return wm_obj


def apply_colorscheme(menu: str, wm: str) -> None:
    if os.path.exists(
        Path(f"~/.config/menu_agnostic__utilities/{wm}/wallpapers.json").expanduser()
    ):
        with open(
            Path(
                f"~/.config/menu_agnostic__utilities/{wm}/wallpapers.json"
            ).expanduser()
        ) as file:
            wallpaper_dict = json.load(file)
    else:
        wallpaper_dict = {
            "catppuccin_macchiato": [
                "pixelart_evening_trees_pole_wires_makrustic.png",
                "pixelart_pokemon_rayquaza_forest_16x9.png",
                "pixelart_seabeach_evening.png",
                "scenery_bridge_river_city.jpg",
            ],
            "dracula": ["pixelart_winter_hut_deer_man_dog_hunt_PixelArtJourney.png"],
            "everblush": ["pixelart_forest_flower.png"],
            "everforest": [
                "scenery_forest_stairs.jpg",
                "scenery_deep_forest_pathway.jpg",
                "everforest-walls_fog_forest_1.jpg",
                "everforest-walls_foggy_valley_1.png",
            ],
            "gruvbox": [
                "pixelart_house_chibi_person_game_jmw327.png",
                "pixelart_house_inside_girl_book_dog_jmw327.png",
                "scenery_astronaut_space_moon_flowers.jpg",
                "pixelart_farm_farmer_warm_color_jmw327.png",
                "pixelart_forest_camp_children_maolow-paoPao.jpg",
            ],
            "matugen": [
                "a_black_sand_beach_with_waves_and_clouds_above.jpg",
                "a_blue_and_pink_gradient_with_white_squares.png",
                "a_building_with_flowers_on_the_balcony.jpg",
                "a_building_with_trees_and_stars_in_the_sky.jpg",
                "a_canal_between_buildings_with_boats.jpg",
                "a_cat_sitting_next_to_a_computer.jpg",
                "a_city_in_the_rain.jpeg",
                "a_close_up_of_a_flower.jpg",
                "a_cup_of_coffee_with_foam.jpg",
                "a_dock_with_trees_and_a_blue_railing.jpg",
                "a_foggy_forest_with_trees_and_bushes.png",
                "a_foggy_landscape_with_trees_and_grass.jpg",
                "a_group_of_birds_flying_in_the_sky.jpg",
                "a_group_of_white_flowers.jpg",
                "a_house_in_the_snow.jpg",
                "a_lake_with_snow_covered_mountains_in_the_background.jpg",
                "a_night_sky_with_clouds_and_a_street_light.jpg",
                "a_road_surrounded_by_trees.jpg",
                "a_road_with_trees_in_the_background.jpg",
                "a_white_light_pole_with_a_jet_trail_in_the_sky.jpg",
                "a_window_with_a_foggy_view.jpg",
                "clouds_above_a_mountain.png",
                "pixelart_dock_no4_house_destroyed_warm_color.png",
                "pixelart_evening_trees_pole_wires_makrustic.png",
                "pixelart_grassland_flowers_field_clouds.png",
                "pixelart_night_boat_duck_lanturn_man__tonbo.png",
                "pixelart_night_cozy_fireflies_stars_dog.png",
                "pixelart_night_stars_clouds_trees_cozy_PixelArtJourney.png",
                "pixelart_pokemon_rayquaza_forest_16x9.png",
                "pixelart_sky_clouds_dog_girl__toyoi_yuuta.png",
                "pixelart_thron_dark_someone.png",
                "scenery_astronaut_space_moon_flowers.jpg",
                "scenery_blue_sea_beach_summer.jpg",
                "scenery_bridge_river_city.jpg",
                "scenery_dark_forest_trees__jr_korpa.jpg",
                "scenery_dark_night_forest_snow_person__winter_in_the_forest__somartist.jpg",
                "scenery_deep_forest_pathway.jpg",
                "scenery_evening_sky_clouds_river__uomi__ai.jpg",
                "scenery_flowers_hill_clouds_colorful_dmitryalexander.jpg",
                "scenery_flower_white_bloom_dark.png",
                "scenery_forest_hut.jpg",
                "scenery_forest_stairs.jpg",
                "scenery_forest_road_light_ray__john_towner.jpg",
                "scenery_green_grass_aesthetic_relaxing.jpg",
                "scenery_japanese_store_walls.jpg",
                "scenery_mist_forest_nord.jpg",
                "scenery_mountain_ice__inno_squirrel__ai.png",
                "scenery_mountain_path_fields__claudio_testa.jpg",
                "scenery_pastel_clouds_dreamlike.jpg",
                "scenery_pokemon_akari_hisuian_growlithe_snorunt_wyrdeer__pixiescout.jpg",
                "scenery_river_tree_forest_evening__inno_squirrel__ai.jpg",
                "scenery_shooting_star_sky_person_evening__uomi__ai.jpg",
                "scenery_space_portal_galaxy.jpg",
                "scenery_star_sky_galaxy.jpg",
                "scenery_tower_sky_landscape.jpg",
                "sunset_with_palm_trees_in_the_foreground__fangpeii.jpg",
            ],
            "nord": [
                "a_house_in_the_snow.jpg",
                "pixelart_night_train_cozy_gas_RoyalNaym_nord.png",
                "scenery_mist_forest_nord.jpg",
                "scenery_pokemon_akari_hisuian_growlithe_snorunt_wyrdeer__pixiescout.jpg",
            ],
            "rose_pine": [
                "pixelart_evening_trees_pole_wires_makrustic.png",
                "pixelart_night_stars_clouds_trees_cozy_PixelArtJourney.png",
                "pixelart_pokemon_rayquaza_forest_16x9.png",
            ],
        }

    colorschemes: dict[str, str] = {
        "[cancel]": "[  Cancel ]",
        "catppuccin_macchiato": " Catppuccin (Macchiato)",
        "dracula": " Dracula",
        "everblush": " Everblush",
        "everforest": " Everforest",
        "gruvbox": " Gruvbox",
        "matugen": " Matugen (Material-You Color Generator)",
        "nord": " Nord",
        "rose_pine": " Rose Pine",
    }

    wm_obj = setup_wm(menu, wm, wallpaper_dict, colorschemes)

    wm_obj.apply(choose_wallpaper=True)


def main():
    wms = ["dwm", "hyprland"]
    menus = ["dmenu", "fuzzel"]

    arg_parser = ArgumentParser(description="change colorscheme")

    # define necessary cli arguments
    arg_parser.add_argument(
        "-m",
        "--menu",
        help="specify the menu launcher",
        choices=menus,
        required=True,
    )
    arg_parser.add_argument(
        "-w",
        "--window-manager",
        help="specify the window manager",
        choices=wms,
        required=True,
    )

    # if no cli arguments are provided, show the help message and exit
    if len(argv) <= 1:
        arg_parser.print_help()
        sys.exit()

    # parse all cli arguments
    args = arg_parser.parse_args()

    # 'window-manager' is accessed by 'window_manager'
    if args.menu and args.window_manager:
        apply_colorscheme(menu=args.menu, wm=args.window_manager)
    else:
        arg_parser.print_help()
        sys.exit()


if __name__ == "__main__":
    main()
