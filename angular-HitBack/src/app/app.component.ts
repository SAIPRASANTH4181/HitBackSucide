import { Component ,Input } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from './services/auth.service';
// import { UsersService } from './services/users.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  @Input() status = '';
  // user$ = this.usersService.currentUserProfile$;
  title: any='angular-HitBack';
  isHome:Boolean = true

  constructor(
    private authService: AuthService,
    private router: Router
  ) {
    
    if(window.location.pathname == "/home") {
      console.log("home")
      this.isHome = true
    }
    else this.isHome = false
  }
ngOnInit() {
  // window.location.reload()
}
  logout() {
    this.router.navigate(['/']);
    this.isHome = false
    // this.authService.logout().subscribe(() => {
    //   // console.log(this.usersService) 
    //   this.router.navigate(['/']);

    // });
  }
}
