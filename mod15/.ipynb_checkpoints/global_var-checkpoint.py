def spam():
    global eggs
    eggs = 'spam'    # this is the global
    
def bacon():
    eggs = 'bacon'   # this is a local
    
def ham():
    print(eggs)  # this is the global

# MAIN
eggs = 42        # this is the global

ham()

bacon()
print(eggs)      # 42

spam()
print(eggs)      # spam
