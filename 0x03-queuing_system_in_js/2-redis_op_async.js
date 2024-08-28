import { createClient, print } from "redis";
import { promisify } from 'util';

const client = createClient();

client
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (error) => {
    console.log("Redis client not connected to the server: ", error);
  });

const getdata = promisify(client.get).bind(client);

const setNewSchool = ( schoolName, value ) => {
    client.set(schoolName, value, print);
}

const displaySchoolValue = async ( schoolName ) => {
    const data = await getdata(schoolName).catch((err) => {
        if (err){
            console.log(err.message);
        }
    });
    console.log(data);
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
