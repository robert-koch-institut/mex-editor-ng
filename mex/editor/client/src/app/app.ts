import { AsyncPipe } from "@angular/common";
import { HttpClient } from "@angular/common/http";
import { Component, inject, signal } from "@angular/core";
import { MatSlideToggle } from "@angular/material/slide-toggle";
import { RouterLink, RouterOutlet } from "@angular/router";

class SampleData {
  title = "";
  text = "";
}

@Component({
  selector: "app-root",
  imports: [RouterOutlet, RouterLink, AsyncPipe, MatSlideToggle],
  templateUrl: "./app.html",
  styleUrl: "./app.scss",
})
export class App {
  protected readonly title = signal("mex-editor");

  private http = inject(HttpClient);

  data$ = this.http.get<SampleData[]>("api/v0/sample-data");
}
