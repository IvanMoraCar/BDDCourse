from behave import then, when, given, step

@step("I go to the 'my account' page")
def I_go_to_the_my_account_page(context):
    print("Hola")