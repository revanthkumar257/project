// Get elements for sign-in and sign-up forms
const signUpButton = document.getElementById('signUpButton');
const signInButton = document.getElementById('signInButton');
const signInForm = document.getElementById('signIn');
const signUpForm = document.getElementById('signup');
const signUpFormElement = document.getElementById('signup-form');
const loginFormElement = document.getElementById('login-form');

const loginBtn = document.querySelector(".login-btn-main");

// Add event listeners for sign-in and sign-up buttons
signUpButton.addEventListener('click', function() {
  signInForm.style.display = "none";
  signUpForm.style.display = "block";
});

signInButton.addEventListener('click', function() {
  signInForm.style.display = "block";
  signUpForm.style.display = "none";
});

// Handle login form submission
loginFormElement.addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById('login-email').value;
  const password = document.getElementById('login-password').value;

  try {
    const response = await fetch('/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password }),
    });

    if (!response.ok) {
      throw new Error('Invalid credentials');
    }

    const responseData = await response.json();

    // Store access token and user details in localStorage
    localStorage.setItem('accessToken', responseData.token);
    localStorage.setItem('user', JSON.stringify(responseData.data));

    // Redirect or perform other actions after successful login
    window.location.href = '/stays'; // Replace with your desired URL

  } catch (error) {
    console.error('Login failed:', error.message);
    // Handle error (e.g., display error message)
  }
});

// Handle signup form submission
signUpFormElement.addEventListener('submit', async (e) => {
  e.preventDefault();

  const fName = document.getElementById('register-fName').value;
  const lName = document.getElementById('register-lName').value;
  const email = document.getElementById('register-email').value;
  const password = document.getElementById('register-password').value;

  try {
    const response = await fetch('/auth/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ fName, lName, email, password }),
    });

    if (!response.ok) {
      throw new Error('Registration failed');

    }else {
        alert("success")

        signInForm.style.display = "block";
        signUpForm.style.display = "none";
    }

  } catch (error) {
    console.error('Registration failed:', error.message);
    // Handle error (e.g., display error message)
  }
});

// Fetch user details using a "me" route
async function fetchMe() {
  const accessToken = localStorage.getItem('accessToken');
  if (!accessToken) {
    console.error('Access token not found.');
    return;
  }

  try {
    const response = await fetch('/auth/me', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${accessToken}`,
      },
    });

    if (!response.ok) {
      throw new Error('Failed to fetch user details');
    }

    const userData = await response.json();
    console.log('User details:', userData);

    // Optionally, update UI with user details
    // e.g., document.getElementById('username').textContent = userData.username;

  } catch (error) {
    console.error('Failed to fetch user:', error.message);
  }
}

