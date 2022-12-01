import { AuthService } from 'src/app/services/auth.service';
import { Component, OnInit,ViewChild,ElementRef} from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { HttpEvent, HttpEventType } from '@angular/common/http';
import { Chart } from "chart.js";
// import { UsersService } from 'src/app/services/users.service';FileUploadService
import * as XLSX from 'xlsx';
import { FileUploadService } from 'src/app/services/file-upload.service';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {
  public chart!: Chart;
  constructor(private fileUploadService: FileUploadService, private toastrService: ToastrService) {}
  ngOnInit(): void {}
  ExcelData : any;
  file : File | any = null;
  progress: number = 0;
  @ViewChild('myInput',{static: true}) myInputVariable!: ElementRef;
  

  // ReadExcel(event:any)
  //   {
  //     let file = event.target.files[0];
  //     let fileReader = new FileReader();
  //     fileReader.readAsBinaryString(file);
  //     fileReader.onload = (e)=>{
  //       var workBook = XLSX.read(fileReader.result,{type:'binary'});
  //       var sheetNames = workBook.SheetNames;
  //       this.ExcelData = XLSX.utils.sheet_to_json(workBook.Sheets[sheetNames[0]]);
  //       console.log(this.ExcelData);
  //     }
  //   }
  
    
  onFileChange(event:any) {
    if (event.target.files.length > 0) {
      this.file = event.target.files[0];
    }
  }

  uploadFile(){
    this.fileUploadService.upload(this.file)
    .subscribe((event: any) => {
        console.log(event)
        this.Barchart(event);
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


  Barchart(arr:any)
  {
      console.log(arr);
      console.log(arr[0]);
      console.log(arr[1]);
      this.chart = new Chart("canvas", {
        type: "bar",
        data: {
          labels: arr[0],
          datasets: [
            {
              label: "# of Votes",
              data: arr[1],
              backgroundColor: [
                "rgba(255, 99, 132, 0.2)",
                "rgba(54, 162, 235, 0.2)",
                "rgba(255, 206, 86, 0.2)",
                "rgba(75, 192, 192, 0.2)",
                "rgba(153, 102, 255, 0.2)",
                "rgba(255, 159, 64, 0.2)",
                "rgba(54, 162, 235, 0.2)",
                "rgba(255, 206, 86, 0.2)",
                "rgba(75, 192, 192, 0.2)",
                "rgba(153, 102, 255, 0.2)",
                "rgba(255, 159, 64, 0.2)"
              ],
              borderColor: [
                "rgba(255, 99, 132, 1)",
                "rgba(54, 162, 235, 1)",
                "rgba(255, 206, 86, 1)",
                "rgba(75, 192, 192, 1)",
                "rgba(153, 102, 255, 1)",
                "rgba(255, 159, 64, 1)",
                "rgba(54, 162, 235, 1)",
                "rgba(255, 206, 86, 1)",
                "rgba(75, 192, 192, 1)",
                "rgba(153, 102, 255, 1)",
                "rgba(255, 159, 64, 1)"
              ],
              borderWidth: 1
            }
          ]
        },
        options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true
                }
              }
            ]
          }
        }
      });
  }
  

}
