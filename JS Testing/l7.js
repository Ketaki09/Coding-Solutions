//Variable Initialization
let datasetObjectMap = 
    {
        "hello": "world",
        "song" : "wild",
        "first" : "1", 
        "second" : "2",
        "Ketaki" : "best"
    }

const valueToBeFoundUsingKey = "Ketaki"

console.info("Variable Initialization completed")

//  Input Param - datasetObjectMap - Object to traverse through
//  Input Param - valueToBeFoundUsingKey - String Value of the key 
//  Output Param - responseValue - Given Key's actual value found in the object
function objectChecker(datasetObjectMap, valueToBeFoundUsingKey){
        if( valueToBeFoundUsingKey in datasetObjectMap){    
            const responseValue = datasetObjectMap[valueToBeFoundUsingKey]
            return responseValue
        }
        else {
            const responseValue = valueToBeFoundUsingKey + " " +"not found in the Object"
            return responseValue
        }
}

console.log(objectChecker(datasetObjectMap, valueToBeFoundUsingKey))
console.info("ObjectChecker Function called successfully")