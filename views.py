from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipes_view(request, dish):
    # Получаем рецепт для указанного блюда
    recipe = DATA.get(dish)
    
    if not recipe:
        # Если рецепт не найден, возвращаем пустой контекст
        context = {'recipe': {}}
        return render(request, 'calculator/index.html', context)
    
    # Создаем копию рецепта для изменения
    recipe_copy = recipe.copy()
    
    # Получаем количество порций из параметра servings
    servings = request.GET.get('servings')
    
    if servings:
        try:
            # Преобразуем servings в целое число
            servings = int(servings)
            if servings > 0:
                # Умножаем все ингредиенты на количество порций
                for ingredient in recipe_copy:
                    recipe_copy[ingredient] = recipe_copy[ingredient] * servings
        except (ValueError, TypeError):
            # Если преобразование не удалось, игнорируем параметр
            pass
    
    # Формируем контекст для шаблона
    context = {
        'recipe': recipe_copy
    }
    
    return render(request, 'calculator/index.html', context)
