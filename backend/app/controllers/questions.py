import random

from flask import jsonify, request
from flask_cors import cross_origin
from app import app
from app.algorithm.ml import ml
from app.algorithm.learning import natu
from app.info import features, questions, answers, questionWithComplete

gYes = [1 for _ in range(8)]
gN = [0 for _ in range(8)]
gPlace = [0 for _ in range(8)]

@app.route('/api/questions/', methods = ['POST'])
@cross_origin()
def getQuestions():
    global gYes
    global gN
    global gPlace

    availableFeatures = features[:]
    characterMatch = None

    if 'alreadyFeatures' in request.json:
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
        gYes, gN, place_id = natu(gYes, gN, gPlace)
        characterMatch = {
          "name": characterMatch['name'][place_id],
          "image": characterMatch['image'][place_id],
        }

        return jsonify(
            characterMatch = characterMatch
        )

    feature = random.choice(availableFeatures)
    param = feature
    question = questions[feature]

    print("***********************")
    print(feature)
    print(question)
    print(answers[feature])
    print("***********************")

    return jsonify(
      feature = feature,
      param = param,
      question = question,
      answers = answers[feature],
      characterMatch = characterMatch
    )