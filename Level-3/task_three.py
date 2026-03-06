# pylint: disable=too-few-public-methods
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


class Question:
    """Question class, contains question, correct answers and chosen answers"""

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        """Stores variables for question"""
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:
    """Quiz class, contains list of questions, name of quiz and type of quiz"""

    def __init__(self, quiz_questions: list, name: str, assessment_type: str):
        """Stores variables for quiz"""
        self.questions = quiz_questions
        self.name = name
        self.assessment_type = assessment_type


class Marking:
    """Marking class, marks quizzes and returns assessment for trainee"""

    def __init__(self, the_quiz: Quiz) -> None:
        """Stores variables for marking"""
        self._quiz = the_quiz

    def mark(self) -> int:
        """Marks the quizzes, gives one correct point for each question,
        returns score as percentage"""
        score = 0
        no_of_questions = len(self._quiz.questions)
        if no_of_questions == 0:
            return 0
        for question in self._quiz.questions:
            if question.chosen_answer == question.correct_answer:
                score += 1
        return (score / no_of_questions) * 100

    def generate_assessment(self) -> Assessment:
        """Creates the assessment for trainees with name, score and type of quiz"""
        if self._quiz.assessment_type == "multiple-choice":
            return MultipleChoiceAssessment(self._quiz.name, self.mark(),
                                            self._quiz.assessment_type)
        if self._quiz.assessment_type == "technical":
            return TechnicalAssessment(self._quiz.name, self.mark(), self._quiz.assessment_type)
        if self._quiz.assessment_type == "presentation":
            return PresentationAssessment(self._quiz.name, self.mark(), self._quiz.assessment_type)
        return None


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
