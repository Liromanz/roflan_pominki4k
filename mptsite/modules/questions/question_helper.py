from mptsite.models import Category_of_questions, Questions, Subcategory_of_questions


class QuestionHelper:

    # структура списка:
    # {
    #   "category": категория - Category_of_questions,
    #   "questions": [вопрос - Questions]
    # }
    @staticmethod
    def get_questions(category: Category_of_questions):
        if category is None:
            return None
        questions_in_filter = Questions.objects.filter(category_id=category).filter(subcategory_id__isnull=True)
        return {"category": category, "questions": list(questions_in_filter)}





    # структура списка:
    # {
    #   "category": категория - Category_of_questions,
    #   "all_questions": [
    #   {
    #       "subcategory": подкатегория - Subcategory_of_questions,
    #       "questions": [вопрос - Questions]
    #   }]
    # }
    @staticmethod
    def get_questions_with_subcategories(category: Category_of_questions):
        if category is None:
            return None
        subcategories = Questions.objects.order_by('subcategory_id').values('subcategory_id').distinct()
        subquestions = []
        for sub in subcategories:
            if sub["subcategory_id"] is not None:
                subcategory = Subcategory_of_questions.objects.get(pk=sub["subcategory_id"])
                subquestions.append({"subcategory": subcategory, "questions": list(
                    Questions.objects.filter(category_id=category).filter(
                        subcategory_id=subcategory))})
        return {"category": category, "all_questions": subquestions}
