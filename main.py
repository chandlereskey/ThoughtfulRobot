# Sort the packages using the following criteria:

# - A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
# - A package is **heavy** when its mass is greater or equal to 20 kg.

# You must dispatch the packages in the following stacks:

# - **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
# - **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
# - **REJECTED**: packages that are **both** heavy and bulky are rejected.

def sort(width, height, length, mass):
  category = "STANDARD"
  volume = width * height * length
  is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
  is_heavy = mass >= 20
  if (is_bulky and not is_heavy) or (is_heavy and not is_bulky):
    category = "SPECIAL"
  elif is_bulky and is_heavy:
    category = "REJECTED"
  return category

print('running unittests')


  
