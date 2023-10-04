import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup(firstName, lastName) {
  const uploadPhotoPromise = uploadPhoto();
  const createUserPromise = createUser(firstName, lastName);

  Promise.all([uploadPhotoPromise, createUserPromise])
    .then(([photoResult, userResult]) => {
      console.log(`${photoResult.body}`);
      console.log(`${userResult.firstName} ${userResult.lastName}`);
    })
    .catch((error) => {
      console.error('Signup system offline', error);
    });
}
