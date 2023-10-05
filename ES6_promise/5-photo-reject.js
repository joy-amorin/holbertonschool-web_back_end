import { uploadPhoto as processUploadPhoto } from "./utils";

export default function uploadPhoto(fileName) {
    return new Promise((reject)=> {
        reject(new Error(`"${fileName}" cannot be processed`))

    });
}