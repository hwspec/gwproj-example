// See README.md for license details.

ThisBuild / scalaVersion     := "2.13.18"
ThisBuild / version          := "0.1.0"
ThisBuild / organization     := "com.github.hwspec"

val chiselVersion = "7.7.0"

lazy val root = (project in file("."))
  .settings(
    name := "gwproj-example",

    resolvers += "central-snapshots" at "https://central.sonatype.com/repository/maven-snapshots/",

    libraryDependencies ++= Seq(
      "io.github.hwspec" %% "garageworks" % "0.4.0-SNAPSHOT",
      "org.chipsalliance" %% "chisel" % chiselVersion,
      "org.scalatest" %% "scalatest" % "3.2.19" % "test",
    ),
    scalacOptions ++= Seq(
      "-language:reflectiveCalls",
      "-deprecation",
      "-feature",
      "-Xcheckinit",
      "-Ymacro-annotations",
    ),
    addCompilerPlugin("org.chipsalliance" % "chisel-plugin" % chiselVersion cross CrossVersion.full),
  )
