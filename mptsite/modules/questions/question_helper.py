from mptsite.models import Category_of_questions, Questions, Subcategory_of_questions


class QuestionHelper:

    def __init__(self, category: Category_of_questions):
        self.category = category

    # структура списка:
    # {
    #   "category": категория - Category_of_questions,
    #   "questions": [вопрос - Questions]
    # }
    def get_questions(self):
        questions_in_filter = Questions.objects.filter(category_id=self.category)
        print(list(questions_in_filter))
        return {"category": self.category, "questions": list(questions_in_filter)}

    # структура списка:
    # {
    #   "category": категория - Category_of_questions,
    #   "all_questions": [
    #   {
    #       "subcategory": подкатегория - Subcategory_of_questions,
    #       "questions": [вопрос - Questions]
    #   }]
    # }
    def get_questions_with_subcategories(self):
        subcategories = Questions.objects.order_by('subcategory_id').values('subcategory_id').distinct()
        subquestions = []
        for sub in subcategories:
            if sub["subcategory_id"] is not None:
                subcategory = Subcategory_of_questions.objects.get(pk=sub["subcategory_id"])
                subquestions.append({"subcategory": subcategory, "questions": list(
                    Questions.objects.filter(category_id=self.category).filter(
                        subcategory_id=subcategory))})
        print(subquestions)
        return {"category": self.category, "all_questions": subquestions}
