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

    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        """Function that returns all assessments of a specified type"""
        assessment_list = []
        for assessment in self.assessments:
            if assessment.type == type:
                assessment_list.append(assessment)
        return assessment_list


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


class MultipleChoiceAssessment(Assessment):
    """Child class of Assessment"""

    def __init__(self, name, score, type="multiple-choice"):
        super().__init__(name, type, score)

    def calculate_score(self):
        """Calculates weighted score for multiple choice assessments"""
        return self.score * 0.7


class TechnicalAssessment(Assessment):
    """Child class of Assessment"""

    def __init__(self, name, score, type="technical"):
        super().__init__(name, type, score)

    def calculate_score(self):
        """Calculates weighted score for technical assessments"""
        return self.score


class PresentationAssessment(Assessment):
    """Child class of Assessment"""

    def __init__(self, name, score, type="presentation"):
        super().__init__(name, type, score)

    def calculate_score(self):
        """Calculates weighted score for presentation assessments"""
        return self.score * 0.6


class Question:

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:

    def __init__(self, quiz: Quiz) -> None:
        self._quiz = quiz
        pass

    def mark(self) -> int:
        score = 0
        no_of_questions = len(self._quiz.questions)
        if no_of_questions == 0:
            return 0
        for question in self._quiz.questions:
            if question.chosen_answer == question.correct_answer:
                score += 1
        return (score / no_of_questions) * 100

    def generate_assessment(self) -> Assessment:
        if self._quiz.type == "multiple-choice":
            return MultipleChoiceAssessment(self._quiz.name, self.mark(), self._quiz.type)
        if self._quiz.type == "technical":
            return TechnicalAssessment(self._quiz.name, self.mark(), self._quiz.type)
        if self._quiz.type == "presentation":
            return PresentationAssessment(self._quiz.name, self.mark(), self._quiz.type)


if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
