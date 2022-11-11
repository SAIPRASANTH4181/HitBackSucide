import { AuthService } from 'src/app/services/auth.service';
import { Component, OnInit,ViewChild,ElementRef} from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { HttpEvent, HttpEventType } from '@angular/common/http';

// import { UsersService } from 'src/app/services/users.service';FileUploadService
import * as XLSX from 'xlsx';
import { FileUploadService } from 'src/app/services/file-upload.service';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {
  constructor(private fileUploadService: FileUploadService, private toastrService: ToastrService) {}
  ngOnInit(): void {}
  ExcelData : any;
  file : File | any = null;
  progress: number = 0;
  @ViewChild('myInput',{static: true}) myInputVariable!: ElementRef;
  

  ReadExcel(event:any)
    {
      let file = event.target.files[0];
      let fileReader = new FileReader();
      fileReader.readAsBinaryString(file);
      fileReader.onload = (e)=>{
        var workBook = XLSX.read(fileReader.result,{type:'binary'});
        var sheetNames = workBook.SheetNames;
        this.ExcelData = XLSX.utils.sheet_to_json(workBook.Sheets[sheetNames[0]]);
        console.log(this.ExcelData);
      }
    }
  
    
  onFileChange(event:any) {
    if (event.target.files.length > 0) {
      this.file = event.target.files[0];
    }
  }

  uploadFile(){
    this.fileUploadService.uploadFile(this.file)
    .subscribe((event: HttpEvent<any>) => {
        this.resetFile();
        switch(event.type){
            case HttpEventType.UploadProgress:
              // this.progress = Math.round(event.loaded / event.total * 100);
              break;
            case HttpEventType.ResponseHeader:
              if(event.status == 200){
                this.toastrService.success("File was uploaded successfully");
                         
              }
              if(event.status == 500){
                this.toastrService.error("Error while uploading file");
              }
        }
    });
  }

  fileIsUploaded()
  {
    let result = false;
    if(this.file && this.file != null )
    {
      result = true;
    }
    return result;
  }

  resetFile()
  {
    this.myInputVariable.nativeElement.value = "";
    this.file = null;
    this.progress = 0;
  }

  
}
