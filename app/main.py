from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    """
    Determines if a group of friends can visit the cafe based on access rules.

    :param friends: A list of visitor dictionaries.
    :param cafe: The Cafe object to visit.
    :returns: A string indicating the group's status.
    """
    masks_to_buy = 0
    vaccine_problem_found = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except NotWearingMaskError:
            masks_to_buy += 1

        except VaccineError:
            vaccine_problem_found = True
            break

        except Exception as e:
            print(f"An unexpected error occurred for "
                  f"{friend.get("name", "a friend")}: {e}")
            break

    if vaccine_problem_found:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
