import { createClient, print }from 'redis;

const client = createClient();

client
    .on("connect", () => {
        console.log("Redis client connected to the server");
    });
    .on("error", (error) => {
        console.log("Redis client not connected to the server: ", error);
    });

const createHash = (hashKey, fieldName, fieldValue) => {
    client.hset(hashKey, fieldName, fieldValue, print);
}


