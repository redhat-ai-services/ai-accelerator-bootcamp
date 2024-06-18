{{/*
Common labels
*/}}
{{- define "phoenix.labels" -}}
app.kubernetes.io/name: {{ include "phoenix.name" . }}
helm.sh/chart: {{ include "phoenix.chart" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app: {{ .Release.Name }}
{{- end -}}

{{/*
Common labels
*/}}
{{- define "labels" -}}
app.kubernetes.io/name: {{ include "phoenix.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{/*
Create a default name that can be overridden by .Values.nameOverride
*/}}
{{- define "phoenix.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "phoenix.chart" -}}
{{ .Chart.Name }}-{{ .Chart.Version }}
{{- end -}}

{{/*
Create the name of the application based on the release name and the chart name.
*/}}
{{- define "phoenix.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else }}
{{- printf "%s-%s" .Release.Name (include "phoenix.name" .) | trunc 63 | trimSuffix "-" -}}
{{- end }}
{{- end -}}

{{/*
Create a name for the service account.
*/}}
{{- define "phoenix.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- if .Values.serviceAccount.name }}
{{- .Values.serviceAccount.name | trunc 63 | trimSuffix "-" -}}
{{- else }}
{{- include "phoenix.fullname" . | trunc 63 | trimSuffix "-" -}}
{{- end }}
{{- else }}
"default"
{{- end }}
{{- end -}}

{{/*
Selector labels for the application
*/}}
{{- define "phoenix.selectorLabels" -}}
app.kubernetes.io/name: {{ include "phoenix.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}
