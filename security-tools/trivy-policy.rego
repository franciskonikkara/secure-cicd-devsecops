package trivy

deny[msg] {
  input.Results[_].Vulnerabilities[_].Severity == "CRITICAL"
  msg := "Critical container vulnerability detected"
}

