"""Sets up Trainee and Assessment classes to keep track of trainees and assessment data"""
from datetime import date, datetime


class Trainee:
    """Trainee class, keeps track of trainees data"""

    def __init__(self, name: str, email: str, date_of_birth: date):
        """Initialises variables for trainee class"""
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = []

    def get_age(self) -> int:
        """Function that returns the age of a trainee"""
        age = datetime.now().year - self.date_of_birth.year
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        """Function that adds an Assessment to the trainees list of assessments"""
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        """Function that returns an assessment that matches the search"""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None


class Assessment:
    """Assessment class, keeps track of data related to assessments"""

    def __init__(self, name: str, type: str, score: float):
        """Initialises variables in assessment class"""
        self.name = name
        self.type = type
        self.score = score
        self.verify_type()
        self.verify_score()

    def verify_type(self):
        """Verifies that the assessment type is valid"""
        if self.type not in ("multiple-choice", "technical", "presentation"):
            raise ValueError("Must be an allowed assessment type")

    def verify_score(self):
        """Verifies that the score is valid"""
        if self.score > 100 or self.score < 0:
            raise ValueError("Must be within score range of 0-100")


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
