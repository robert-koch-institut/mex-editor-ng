import type { ComponentFixture } from "@angular/core/testing";
import { TestBed } from "@angular/core/testing";
import { provideRouter } from "@angular/router";

import { Subpage } from "./subpage";

describe("Subpage", () => {
  let component: Subpage;
  let fixture: ComponentFixture<Subpage>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Subpage],
      providers: [provideRouter([])],
    }).compileComponents();

    fixture = TestBed.createComponent(Subpage);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it("should create", () => {
    expect(component).toBeTruthy();
  });
});
