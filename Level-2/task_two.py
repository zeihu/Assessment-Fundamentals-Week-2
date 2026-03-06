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
        if not isinstance(assessment, Assessment):
            raise TypeError("You must enter an Assessment class assessment")
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        """Function that returns an assessment that matches the search"""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None

    def get_assessment_of_type(self, assessment_type: str) -> list[Assessment]:
        """Function that returns all assessments of a specified type"""
        assessment_list = []
        for assessment in self.assessments:
            if assessment.assessment_type == assessment_type:
                assessment_list.append(assessment)
        return assessment_list


class Assessment:
    """Assessment class, keeps track of data related to assessments"""

    def __init__(self, name: str, assessment_type: str, score: float):
        """Initialises variables in assessment class"""
        self.name = name
        self.assessment_type = assessment_type
        self.score = score
        self.verify_assessment_type()
        self.verify_score()

    def verify_assessment_type(self):
        """Verifies that the assessment type is valid"""
        if self.assessment_type not in ("multiple-choice", "technical", "presentation"):
            raise ValueError("Must be an allowed assessment type")

    def verify_score(self):
        """Verifies that the score is valid"""
        if self.score > 100 or self.score < 0:
            raise ValueError("Must be within score range of 0-100")


class MultipleChoiceAssessment(Assessment):
    """Child class of Assessment"""

    def __init__(self, name, score, assessment_type="multiple-choice"):
        super().__init__(name, assessment_type, score)

    def calculate_score(self):
        """Calculates weighted score for multiple choice assessments"""
        return self.score * 0.7


class TechnicalAssessment(Assessment):
    """Child class of Assessment"""

    def __init__(self, name, score, assessment_type="technical"):
        super().__init__(name, assessment_type, score)

    def calculate_score(self):
        """Calculates weighted score for technical assessments"""
        return self.score


class PresentationAssessment(Assessment):
    """Child class of Assessment"""

    def __init__(self, name, score, assessment_type="presentation"):
        super().__init__(name, assessment_type, score)

    def calculate_score(self):
        """Calculates weighted score for presentation assessments"""
        return self.score * 0.6


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
