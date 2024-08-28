/**
 * a script that connect to the Redis server running on your machine
 *
 * and displays:
 * Redis client connected to the server when
 * the connection to Redis works correctly
 * else
 * Redis client not connected to the server: ERROR_MESSAGE
 * when the connection to Redis does not work
 */

import { createClient } from "redis";

const client = createClient();

client
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (error) => {
    console.log("Redis client not connected to the server: ", error);
  });
