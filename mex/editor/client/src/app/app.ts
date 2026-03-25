import { AsyncPipe } from "@angular/common";
import { HttpClient } from "@angular/common/http";
import { Component, inject, signal } from "@angular/core";
import { RouterOutlet } from "@angular/router";

class SampleData {
  title = "";
  text = "";
}

@Component({
  selector: "app-root",
  imports: [RouterOutlet, AsyncPipe],
  templateUrl: "./app.html",
  styleUrl: "./app.scss",
})
export class App {
  protected readonly title = signal("mex-editor");

  private http = inject(HttpClient);

  data$ = this.http.get<SampleData[]>("http://127.0.0.1:8000/api/v0/sample-data");
}
