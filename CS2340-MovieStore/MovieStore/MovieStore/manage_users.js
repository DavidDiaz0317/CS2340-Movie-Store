const admin = require("firebase-admin");
admin.initializeApp();

// List users
async function listUsers() {
    const listUsersResult = await admin.auth().listUsers(100);
    listUsersResult.users.forEach(user => {
        console.log(user.uid, user.email);
    });
}

// Create a user
async function createUser(email, password) {
    const user = await admin.auth().createUser({
        email: email,
        password: password
    });
    console.log("Created user:", user.uid);
}

// Update a user
async function updateUser(uid, updates) {
    await admin.auth().updateUser(uid, updates);
    console.log("User updated.");
}

// Delete a user
async function deleteUser(uid) {
    await admin.auth().deleteUser(uid);
    console.log("User deleted.");
}