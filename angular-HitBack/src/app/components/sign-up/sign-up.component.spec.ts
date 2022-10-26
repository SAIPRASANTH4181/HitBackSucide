import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientModule } from '@angular/common/http';
import { SignUpComponent } from './sign-up.component';
import { FIREBASE_OPTIONS } from '@angular/fire/compat';
import { environment } from 'src/environments/environment';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule } from '@angular/forms';
describe('SignUpComponent', () => {
  let component: SignUpComponent;
  let fixture: ComponentFixture<SignUpComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SignUpComponent ],
      imports:[HttpClientModule,RouterTestingModule,ReactiveFormsModule],
      providers: [{ provide: FIREBASE_OPTIONS, useValue: environment.firebase}],
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SignUpComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('valid form', ()=>{
    component.signUpForm.controls['name'].setValue('test')
    component.signUpForm.controls['email'].setValue('a@gmail.com')
    component.signUpForm.controls['password'].setValue('qwerty123')
    component.signUpForm.controls['confirmPassword'].setValue('qwerty123')
    expect(component.signUpForm.valid).toBeTruthy();
  });

  it('invalid form ', ()=>{
    component.signUpForm.controls['email'].setValue('a@mail')
    component.signUpForm.controls['password'].setValue('qw')
    component.signUpForm.controls['confirmPassword'].setValue('qwe')
    expect(component.signUpForm.valid).toBeFalsy();
  });

  it('empty invalid form', ()=>{
    component.signUpForm.controls['name'].setValue('')
    component.signUpForm.controls['email'].setValue('')
    component.signUpForm.controls['password'].setValue('')
    component.signUpForm.controls['confirmPassword'].setValue('')
    expect(component.signUpForm.valid).toBeFalsy();
  });

});
