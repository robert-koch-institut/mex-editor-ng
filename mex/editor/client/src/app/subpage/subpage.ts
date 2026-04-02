// import { AsyncPipe } from "@angular/common";
import { Component, inject } from "@angular/core";
import { ActivatedRoute } from "@angular/router";
// import { startWith, switchMap } from "rxjs";

@Component({
  selector: "app-subpage",
  // imports: [AsyncPipe],
  templateUrl: "./subpage.html",
  styleUrl: "./subpage.scss",
})
export class Subpage {
  private activatedRoute = inject(ActivatedRoute);
  title = this.activatedRoute.snapshot.data["title"] || "WHY...";
}
