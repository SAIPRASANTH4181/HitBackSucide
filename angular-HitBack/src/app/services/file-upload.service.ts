import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class FileUploadService {

  // Declare backend url 
  uri = 'http://127.0.0.1:5000';
  
  // Passing arguments to constructor
  constructor(private http: HttpClient) { }

  // Function gets called when clicked on upload
  upload(file:File){
    console.log(file)
    var form = new FormData();

    // Append csv file 
    form.append("file",file,file.name)
    let headers = new HttpHeaders({
      'file': file.name
       });
  
    return this.http.post(`${this.uri}`,form,{headers})
  }}
