'use strict';

const mockData = require('./mockData.js').data;

// Your code here
const profile = {
  first_name: "", 
  last_name: "", 
  age: 0, 
  gender: "", 
  gender_interest: "", 
  location: "", 
  min_age_interest: 0, 
  max_age_interest: 0,
};

//  The questions and its loops

const questionList = ["What first name do you go by?", "What is your last name?", "How old are you?", "What gender do you identify with? (M / F / X)", "What gender are you interested in dating? (M / F / X)", "Do you live in a city or rural?", "Minimum age of interest? (18 - 99)", "Maximum age of interest? (18 - 99)"];

function createProfile() {
  // //  First name
  let first_name = prompt(questionList[0]);
  var hasNumber = /\d/;
  if (hasNumber.test(first_name) == true) {
    first_name = prompt(questionList[0]);
  }
  while (first_name == "") {
    first_name = prompt(questionList[0]);
  }
  profile.first_name = first_name;
  
  // //  last_name
  let last_name = prompt(questionList[1]);
  var hasNumber = /\d/;
  if (hasNumber.test(last_name) == true) {
    last_name = prompt(questionList[0]);
  }
  while (last_name == "") {
    last_name = prompt(questionList[1]);
  }
  profile.last_name = last_name;
  
  // //  age
  let age = prompt(questionList[2]);
  var letters = /[a-zA-Z]/g;
  while (letters.test(age) == true) {
    age = prompt(questionList[2]);
  }
  while (age < 18) {
    age = prompt(questionList[2]);
  }
  profile.age = age;
  
  // //  gender
  let gender = prompt(questionList[3]);
  while (gender != "M" && gender != "F" && gender != "X") {
    gender = prompt(questionList[3]);
  }
  profile.gender = gender;
  
  // //  gender interest
  let gender_interest = prompt(questionList[4]);
  while (gender_interest != "M" && gender_interest != "F" && gender_interest != "X") {
    gender_interest = prompt(questionList[4]);
  }
  profile.gender_interest = gender_interest;
  
  // // location
  let location = prompt(questionList[5]);
  while (location.toLocaleLowerCase() != "city" && location.toLocaleLowerCase() != "rural") {
    location = prompt(questionList[5]);
  }
  profile.location = location;
  
  // //  min age interesest
  let min_age_interest = prompt(questionList[6]);
  var hasLetter = /[a-zA-Z]/g;
  while (hasLetter.test(min_age_interest) == true) {
    min_age_interest = prompt(questionList[2]);
  }
  while (min_age_interest < 18) {
    min_age_interest = prompt(questionList[6]);
  }
  profile.min_age_interest = min_age_interest;
  
  // // max age interesest
  let max_age_interest = prompt(questionList[7]);
  var letters = /[a-zA-Z]/g;
  while (letters.test(max_age_interest) == true) {
    max_age_interest = prompt(questionList[2]);
  }
  while (max_age_interest > max_age_interest) {
    max_age_interest = prompt(questionList[7]);
  }
  profile.max_age_interest = max_age_interest;
  console.log(`Welcome to our dating app ${profile.first_name}`)
  return profile;
}


function filterProfiles(profile) {
  let filtered_list = []
  for (let i = 0; i < mockData.length; i++){
    if ((mockData[i].min_age_interest < profile.age && profile.age < mockData[i].max_age_interest) && (profile.min_age_interest < mockData[i].age && mockData[i].age < profile.max_age_interest) && (profile.location == mockData[i].location) && (profile.gender == mockData[i].gender_interest && mockData[i].gender == profile.gender_interest))
    { 
      filtered_list.push(mockData[i]); 
    }
  }
  if (filtered_list.length == 0) {
    console.log("Sorry we could not find any matching profiles!");
  } else {
    console.log(`We have found ${filtered_list.length} matching profiles: \n`);
    for (let j = 0; j < filtered_list.length; j ++) {
      console.log(`${j + 1}. ${filtered_list[j].first_name} ${filtered_list[j].first_name} is ${filtered_list[j].age} years old and lives ${filtered_list[j].location}`);
    }
  }
}


createProfile();
filterProfiles(profile);