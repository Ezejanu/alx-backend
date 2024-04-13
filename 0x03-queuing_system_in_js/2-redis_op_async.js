import redis from 'redis';
import { promisify } from 'util';

// Create Redis client
const client = redis.createClient();

// Promisify get method
const getAsync = promisify(client.get).bind(client);

// Event listener for sccessful connection
client.on('connect', () => {
	console.log('Redis client connected to the server');
});

// Event listener for connection error
client.on('error', (error) => {
	console.error(`Redis client not connected to the server: ${error}`);
});

// Function to set a new school in Redis
const setNewSchool = (schoolName, value) => {
	client.set(schoolName, value, redis.print);
};

// Function to display the value of a school
const displaySchoolValue = (schoolName) => {
	client.get(schoolName, (error, value) => {
		if (error) {
			console.error(`Error getting value for ${schoolName}: ${error}`);
		} else {
			console.log((`Value for ${schoolName}: ${value}`);
		}
	});
};

// Call functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
