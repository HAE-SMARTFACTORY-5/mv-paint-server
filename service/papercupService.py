from repository import papercupRepository

def findAllPapercup():
    return papercupRepository.findAll()

def findByPapercupId(papercupId):
    return papercupRepository.findById(papercupId)