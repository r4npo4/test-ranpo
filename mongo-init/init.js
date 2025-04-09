db = db.getSiblingDB('test');
db.users.deleteMany({})  
db.users.insertOne({
  username: "admin",
  password: "admin"
});
