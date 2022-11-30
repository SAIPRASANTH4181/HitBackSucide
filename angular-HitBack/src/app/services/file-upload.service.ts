import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class FileUploadService {

  uri = 'http://127.0.0.1:5000';
  
  constructor(private http: HttpClient) { }

  uploadFile(file:File){
 
    var form = new FormData();
    form.append("file",file,file.name)
    let headers = new HttpHeaders({
      'file': file.name
       });
  
    return this.http.post(`${this.uri}`,form,{
      headers,reportProgress : true,observe: 'events'})
  }}
