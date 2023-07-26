# name, adjective, noun
mad_libs = "{} laughed at the {} {}."

# relative position(order matters & first three) insufficient number of args will cause error
print(mad_libs.format("bobby", "green", "alien"))

mad_libs = "{0} laughed at the {1} {2}."

print(mad_libs.format("bobby", "green", "alien"))

mad_libs = "{2} laughed at the {1} {0}."

print(mad_libs.format("bobby", "green", "alien"))

# args with keyword param(use this approach)
mad_libs = "{name} laughed at the {adjective} {noun}."

print(mad_libs.format(name = "bobby", adjective = "green", noun = "alien"))

name = input("enter name: ")

adjective = input("enter adjective: ")

noun = input("enter noun: ")

print(mad_libs.format(name = name, adjective = adjective, noun = noun))




