from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def splash_screen(request):
    """Splash screen view"""
    return render(request, "splash.html")


def login_page(request):
    if (request.method == "POST"):
        u_name = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=u_name).exists():
            messages.error(request, "Invalid User Name")
            return redirect("login_page")

        user = authenticate(request, username=u_name, password=password)

        if user is None:
            messages.error(request, "Inavlid Password")
            return redirect("login_page")
        else:
            login(request, user)
            return redirect("/recipe_view/")

    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("/login_page/")


def signup_page(request):
    if (request.method == "POST"):
        f_name = request.POST.get("first_name")
        l_name = request.POST.get("last_name")
        u_name = request.POST.get("username")
        password = request.POST.get("password")
        con_password = request.POST.get("confirm_password")

        user = User.objects.filter(username=u_name)
        # print(
        #     f"""first name : {f_name} last name : {l_name}  user name : {u_name}  password: {password}  confirm Password : {confirm_password}  """)
        if (user.exists()):
            messages.error(request, "User Al ready Exist")
            return redirect("signup_page")

        if (password != con_password):
            messages.error(request, "Password Does't Match")
            return redirect("signup_page")

        try:
            validate_password(password)
        except ValidationError as e:
            for error in e.messages:
                messages.error(request, error)
            return redirect("signup_page")

        user = User.objects.create_user(
            first_name=f_name,
            last_name=l_name,
            username=u_name,
            password=password,
        )

        # user.set_password(password)
        # user.save()

        messages.success(request, "Account Created Succesfully")

        return redirect("signup_page")
    return render(request, "signup.html")


@login_required(login_url="/login_page/")
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


@login_required(login_url="/login_page/")
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    messages.success(request, "Recipe Deleted Successfully 🗑️")
    return redirect("recipe-view")


@login_required(login_url="/login_page/")
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
