from argparse import ArgumentParser


def add_argument(parser: ArgumentParser):
    parser.add_argument(
        "--experiment_name",
        default="new",
        type=str,
    )
    parser.add_argument(
        "--loss",
        default="dice",
        choices=[
            "dice",
            "bce",
            "diceCE",
            "focal",
            "dice_focal",
            "Hausdorff",
            "dice_focal_Hausdorff",
        ],
        type=str,
    )
    parser.add_argument(
        "--diceCE_lambda_dice",
        default=1,
        type=float,
    )
    parser.add_argument(
        "--diceCE_lambda_CE",
        default=1,
        type=float,
    )
    parser.add_argument(
        "--focal_gamma",
        default=2,
        type=float,
    )
    parser.add_argument(
        "--focal_alpha",
        default=0.1,
        type=float,
    )
    parser.add_argument(
        "--focal_dice_lambda_dice",
        default=0.8,
        type=float,
    )
    parser.add_argument(
        "--focal_dice_lambda_focal",
        default=0.2,
        type=float,
    )
