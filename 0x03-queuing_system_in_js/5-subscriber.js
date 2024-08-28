import { createClient, print }from 'redis';

const client = createClient();

client
    .on("connect", () => {
        console.log("Redis client connected to the server");
    })
    .on("error", (error) => {
        console.log("Redis client not connected to the server: ", error);
    });


client.subscribe('holberton school channel');

//listen for messages on channel and print message when received
client.on('message', function (channel, message) {
  console.log(message);

  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.end(true);
  }
});
