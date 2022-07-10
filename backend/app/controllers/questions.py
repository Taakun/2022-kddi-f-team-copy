import random

from flask import Flask, jsonify, request, session
from flask_cors import cross_origin
from app import app
from app.algorithm.ml import ml
from app.algorithm.learning import natu
from app.info import features, questions, answers, questionWithComplete

gFeatures = ['summerresort', 'fruit', 'meat', 'water', 'emotionalspace']

gQuestions = {
  'summerresort': '避暑地に行きたいですか?',
  'fruit': '果物は好きですか?',
  'meat': '肉食ですか?',
  'water': '水は好きですか?',
  'emotionalspace': 'エモい空間は好きですか?',
}

gAnswers = {
  'summerresort': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'fruit': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'meat': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'water': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'emotionalspace': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
}

@app.route('/api/questions/', methods = ['POST'])
@cross_origin()
def getQuestions():
    global gFeatures
    global gQuestions
    global gAnswers

    availableFeatures = gFeatures[:]
    characterMatch = None

    if 'alreadyFeatures' in request.json:
        print(request.json['alreadyFeatures'])

        availableFeatures = set(availableFeatures) - set(request.json['alreadyFeatures'])
        availableFeatures = list(availableFeatures)

        featuresThatCharacterIsTrue = []

        characterMatch = ml(request.json['alreadyFeatures'], request.json['params'], request.json['answers'])
        characterMatch = characterMatch.to_dict()

        characterMatchId = 0
        for id in characterMatch['name']:
            characterMatchId = id

        for i in range(len(availableFeatures)):
            availableFeature = availableFeatures[i]
            if(characterMatch[availableFeature][characterMatchId]):
                featuresThatCharacterIsTrue.append(availableFeature)
        
        if(len(featuresThatCharacterIsTrue)):
            availableFeatures = featuresThatCharacterIsTrue

        characterMatch = {
          "name": characterMatch['name'][characterMatchId],
          "image": characterMatch['image'][characterMatchId],
        }

    if(not len(availableFeatures)):
        return jsonify(
            characterMatch = characterMatch
        )

    feature = random.choice(availableFeatures)
    param = feature
    question = gQuestions[feature]

    return jsonify(
      feature = feature,
      param = param,
      question = question,
      answers = gAnswers[feature],
      characterMatch = characterMatch
    )

@app.route('/api/learning/', methods = ['POST'])
@cross_origin()
def learning():
    print("not completed.")