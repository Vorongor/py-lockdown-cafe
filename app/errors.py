class VaccineError(Exception):
    """Mani exception that raised when some vaccine trouble"""


class NotVaccinatedError(VaccineError):
    """Visitor has no vaccine"""


class OutdatedVaccineError(VaccineError):
    """Visitors vaccine run out date"""


class NotWearingMaskError(Exception):
    """Visitor do not weare a face-mask"""
