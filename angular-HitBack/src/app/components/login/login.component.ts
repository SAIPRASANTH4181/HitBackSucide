import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { NonNullableFormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { HotToastService } from '@ngneat/hot-toast';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements OnInit {
  @Output() newItemEvent = new EventEmitter<boolean>();

  // Declare form variables
  loginForm = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', Validators.required],
  });

// Passing arguments to constructor
  constructor(
    private authService: AuthService,
    private toast: HotToastService,
    private router: Router,
    private fb: NonNullableFormBuilder
  ) {}

  ngOnInit(): void {}

  // To get email address from form
  get email() {
    return this.loginForm.get('email');
  }

  // To get password from form
  get password() {
    return this.loginForm.get('password');
  }

  // On submit of the form
  submit() {
    const { email, password } = this.loginForm.value;

    // Check whether email or password have value or not
    if (!this.loginForm.valid || !email || !password) {
      return;
    }

    // Connect to auth service
    this.authService.login(email, password)
      .pipe(
        this.toast.observe({
          success: 'Logged in successfully',
          loading: 'Logging in...',
          error: ({ message }) => `There was an error: ${message} `,
        })
      )
      .subscribe(() => {
        this.router.navigate(['/home']);
        this.newItemEvent.emit(true);
      });
  }
}
