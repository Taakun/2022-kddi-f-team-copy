# Features
features = ['summerresort', 'fruit', 'meat', 'water', 'emotionalspace']

# Questions
questions = {
  'summerresort': '避暑地に行きたいですか?',
  'fruit': '果物は好きですか?',
  'meat': '肉食ですか?',
  'water': '水は好きですか?',
  'emotionalspace': 'エモい空間は好きですか?',
}

# Answers Buttons
answers = {
  'summerresort': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'fruit': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'meat': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'water': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'emotionalspace': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
}

# Answers that is String
questionWithComplete = []

# Absolute (Remove train_x item if is not equal)
absoluteFeatures = []