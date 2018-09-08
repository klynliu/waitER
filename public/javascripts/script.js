var getdata = require('./getdata')
require('./triage')

var headers = {
    'Authorization': 'Bearer ' + 'demo',
    'Accept': 'application/json'
};
var url = 'https://api.humanapi.co/v1/human/activities/summaries?access_token=demo&source=myfitnesspal&limit=10'

getdata.getUserData(url, headers, function (error, data) {
    console.log(error)
    console.log(data)
})

