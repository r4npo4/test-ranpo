// mongo-init/init.js
db = db.getSiblingDB('test');  // use 'test' database
db.users.insertOne({
    username: "admin",
    password: "admin"
});
