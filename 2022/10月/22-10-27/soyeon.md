## 오늘 짠 코드
### 람다 -> rds update코드
const AWS = require('aws-sdk')
AWS.config.update({ region:"ap-northeast-2"})
const s3 = new AWS.S3()
var mariadb = require('mariadb');

var pool = mariadb.createPool({
    host: 'idiot-root.c35pvkgak4n8.ap-northeast-2.rds.amazonaws.com',
    user: 'root',
    password: 'h13001212!',
    database: 'idiot'
})

exports.handler = async (event, context) => {

    // Get the object from the event and show its content type
    const bucket = event.Records[0].s3.bucket.name;
    const key = decodeURIComponent(event.Records[0].s3.object.key.replace(/\+/g, ' '));
    const params = {
        Bucket: bucket,
        Key: key,
    };
    const URL = "https://idiot-model-bucket.s3.ap-northeast-2.amazonaws.com/" + key;
    console.log(`URL!!!!`,URL);

    const conn = await pool.getConnection();
    conn.query('USE idiot');
    
    const estateId = key.split('/')[1];
    console.log(`estateId!!!!`,estateId)
    
    const updateQuery = 'UPDATE estate SET MODEL = \'' + URL + '\' WHERE ESTATE_ID = ' + estateId + ';';
    console.log(`updateQuery!!!!`,updateQuery)
    
    conn.query(updateQuery, function(error,results,fields){
        if(error) {
            console.log(error);
        }
        console.log(results);
    });

    conn.end();
};
