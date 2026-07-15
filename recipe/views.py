from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from django.contrib import messages


def splash_screen(request):
    """Splash screen view"""
    return render(request, "splash.html")


def recipe_view(request):
    if request.method == "POST":
        recipe_name = request.POST.get("recipe_name")
        recipe_description = request.POST.get("recipe_description")
        recipe_img = request.FILES.get("recipe_img")

        if recipe_name and recipe_description:
            Recipe.objects.create(
                recipe_name=recipe_name,
                recipe_description=recipe_description,
                recipe_img=recipe_img
            )
            messages.success(request, "Recipe Added Successfully 🎉")
        else:
            messages.error(request, "Please fill all required fields!")

        return redirect("recipe-view")

    recipes = Recipe.objects.all().order_by("-id")

    # Search functionality
    search_query = request.GET.get("search_re")
    if search_query:
        recipes = recipes.filter(recipe_name__icontains=search_query)
        if not recipes:
            messages.info(request, f"No recipes found for '{search_query}'")

    return render(request, "recipe.html", {
        "recipes": recipes,
        "search_query": search_query  # Pass search query to template
    })


def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    messages.success(request, "Recipe Deleted Successfully 🗑️")
    return redirect("recipe-view")


def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == "POST":
        recipe_name = request.POST.get("recipe_name")
        recipe_description = request.POST.get("recipe_description")

        if recipe_name and recipe_description:
            recipe.recipe_name = recipe_name
            recipe.recipe_description = recipe_description

            if request.FILES.get("recipe_img"):
                recipe.recipe_img = request.FILES.get("recipe_img")

            recipe.save()
            messages.success(request, "Recipe Updated Successfully 🎉")
        else:
            messages.error(request, "Please fill all required fields!")

        return redirect("recipe-view")

    return render(request, "update_recipe.html", {"recipe": recipe})
