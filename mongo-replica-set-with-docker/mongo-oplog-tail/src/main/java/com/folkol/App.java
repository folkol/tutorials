package com.folkol;

import com.mongodb.BasicDBObject;
import com.mongodb.CursorType;
import com.mongodb.MongoClient;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoCollection;
import org.bson.BSONObject;
import org.bson.BsonTimestamp;
import org.bson.Document;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Properties;

public class App {
    public static void main(String[] args) throws IOException {
        Properties props = new Properties();
        File file = new File("state.properties");
        if(!file.exists()) {
            file.createNewFile();
        }
        FileInputStream fis = new FileInputStream(file);
        props.load(fis);
        fis.close();
        String timestamp = props.getProperty("timestamp");
        System.out.println(timestamp);
        String inc = props.getProperty("inc");
        System.out.println(inc);

        MongoCollection<Document> local = new MongoClient()
                .getDatabase("local")
                .getCollection("oplog.rs");

        BsonTimestamp bsonTimestamp = new BsonTimestamp(Integer.parseInt(timestamp), Integer.parseInt(inc) + 10);
        BSONObject bsonObject = new BasicDBObject();
        bsonObject.put("ts", bsonTimestamp);
        FindIterable<Document> documents = local.find(bsonObject)
                .cursorType(CursorType.Tailable)
                .noCursorTimeout(true);

        for(Document d : documents) {
            System.out.println(d);
            BsonTimestamp ts = (BsonTimestamp) d.get("ts");
            props.setProperty("timestamp", Integer.toString(ts.getTime()));
            props.setProperty("inc", Integer.toString(ts.getInc()));
            props.store(new FileOutputStream(file), "lollers");
        }
    }
}
