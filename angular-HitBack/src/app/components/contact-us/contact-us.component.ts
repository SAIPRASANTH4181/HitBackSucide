import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { NonNullableFormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { HotToastService } from '@ngneat/hot-toast';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-contact-us',
  templateUrl: './contact-us.component.html',
  styleUrls: ['./contact-us.component.css']
})
export class ContactUsComponent implements OnInit {
  @Output() newItemEvent = new EventEmitter<boolean>();

  // Declare form variables
  contactForm = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    message: ['', Validators.required],
  });

  // Passing arguments to constructor
  constructor(
    private authService: AuthService,
    private toast: HotToastService,
    private router: Router,
    private fb: NonNullableFormBuilder
  ) { }

  ngOnInit(): void {
  }

  // To get email address
  get email() {
    return this.contactForm.get('email');
  }

  // To get message from form
  get message() {
    return this.contactForm.get('message');
  }


  // On submit of the form
  submit() {
    const { email, message } = this.contactForm.value;

    if (!this.contactForm.valid || !email || !message) {
      return;
    }
  }

}
